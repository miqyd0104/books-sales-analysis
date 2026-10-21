"""Download the chosen Kaggle CSV and verify the recorded source snapshot."""
from pathlib import Path
import hashlib
import io
import json
import ssl
import certifi
import urllib.error
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parents[1]

def main():
    manifest = json.loads((ROOT / "data/raw/manifest.json").read_text())
    target = ROOT / "data/raw" / manifest["filename"]
    if target.exists():
        content = target.read_bytes()
    else:
        request = urllib.request.Request(manifest["download_url"], headers={"User-Agent": "books-sales-analysis/1.0"})
        try:
            with urllib.request.urlopen(request, timeout=60, context=ssl.create_default_context(cafile=certifi.where())) as response:
                archive = response.read()
            with zipfile.ZipFile(io.BytesIO(archive)) as dataset:
                content = dataset.read(manifest["filename"])
        except (urllib.error.URLError, zipfile.BadZipFile, KeyError) as exc:
            raise SystemExit("Download failed. Download the CSV from the Kaggle source page into data/raw/. " + str(exc)) from exc
    digest = hashlib.sha256(content).hexdigest()
    if digest != manifest["sha256"]:
        raise SystemExit("CSV checksum differs from the recorded snapshot. Review the source version before updating manifest.json; no file was overwritten.")
    if not target.exists():
        target.write_bytes(content)
    print(f"Verified dataset: {target.name}")

if __name__ == "__main__":
    main()
