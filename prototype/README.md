# AushadhAI Prototype

This folder contains a small full-stack prototype for AI-assisted drug discovery.

The app lets a user:

- upload a protein pocket file as `.pdb`
- request molecule generation
- view generated molecules in 3D
- inspect simple drug-likeness metrics
- download generated `.sdf` files

The prototype is designed as a demo-friendly system, not a production deployment.

## What's In This Folder

- `app.py`
  Backend server built with FastAPI. It accepts uploads, creates per-request job folders, reads molecule files, computes RDKit metrics, and returns JSON to the frontend.

- `web/index.html`
  Frontend UI. This is a single-file web app containing HTML, CSS, and JavaScript. It handles file upload, form submission, result rendering, and 3D visualization with `3Dmol.js`.

- `generated/source/`
  Demo molecule source folder. If `.sdf` files exist here, the backend uses them in demo mode instead of calling the live PMDM model.

- `jobs/`
  Stores one folder per generation request. Each job folder contains the uploaded `.pdb`, generated or copied `.sdf` files, and a `result.json` file.

- `uploads/`
  Reserved upload directory. In the current implementation, uploaded `.pdb` files are saved into the per-job folder instead.

- `requirements.txt`
  Python dependencies needed to run the backend.

- `SETUP_GUIDE.txt`
  Beginner-friendly setup walkthrough. Keep this if you want step-by-step instructions for a first-time local run.

## Architecture

This prototype has two main parts:

- Frontend: `web/index.html`
- Backend: `app.py`

High-level flow:

1. User uploads a `.pdb` file in the browser.
2. Frontend sends a `POST /generate` request to the backend.
3. Backend creates a new job folder in `jobs/<job_id>/`.
4. Backend gets molecule `.sdf` files from either demo mode or live mode.
5. Backend computes metrics with RDKit and builds a JSON response.
6. Frontend renders molecule cards, metrics, download buttons, and 3D viewers.

## Backend Overview

The backend in `app.py` exposes these main routes:

- `GET /`
  Redirects to the frontend UI.

- `GET /health`
  Returns basic health info, including whether RDKit is available and how many demo `.sdf` files were found.

- `POST /generate`
  Main generation endpoint. Accepts:
  - `pdb_file`
  - `num_atom`
  - `num_samples`

- `GET /job/{job_id}`
  Returns the saved result JSON for a previous job.

- `GET /sdf/{job_id}/{filename}`
  Serves an `.sdf` file for download.

Important backend behavior:

- Validates that the uploaded file ends with `.pdb`
- Creates a unique short job id
- Saves uploaded input into a job folder
- Computes molecule metrics using RDKit
- Stores results in `jobs/<job_id>/result.json`

## Frontend Overview

The frontend is a single-page demo interface inside `web/index.html`.

It includes:

- a landing page and project story sections
- a live demo section for uploading `.pdb` files
- client-side validation for file type and numeric inputs
- `fetch()` calls to the backend
- result cards showing:
  - QED
  - molecular weight
  - LogP
  - atom count
  - Lipinski rule summary
  - SMILES
  - SDF download button
- 3D molecule rendering using `3Dmol.js`

The GNN evaluation section in the frontend is currently static and presentation-oriented. Its experiment numbers are hardcoded in the page and are not being computed live by the backend.

## Demo Mode vs Live Mode

The backend supports two operating styles.

### Demo Mode

If `.sdf` files are present in `generated/source/`, the backend uses those files directly.

This is the easiest way to run the prototype locally because it does not require the real PMDM generation environment to be available.

### Live Mode

If the configured Colab or Drive paths exist, the backend can attempt to call the PMDM sampling script through `subprocess.run(...)`.

These paths are defined near the top of `app.py`:

- `DRIVE_BASE`
- `COLAB_PYTHON`
- `COLAB_CKPT`
- `COLAB_REPO`

In the current state of the prototype, demo mode is the practical default.

## Requirements

The backend depends on:

- `fastapi`
- `uvicorn`
- `python-multipart`
- `rdkit`

Install from `requirements.txt`:

```powershell
pip install -r requirements.txt
```

If `rdkit` gives installation trouble, see `SETUP_GUIDE.txt` for alternatives.

## How To Run

From this folder:

```powershell
python app.py
```

Then open:

```text
http://localhost:8000
```

If the frontend does not load at `/`, try:

```text
http://localhost:8000/ui/
```

## Basic Usage

1. Start the backend with `python app.py`
2. Open the app in the browser
3. Upload a `.pdb` file
4. Choose `num_atom` and `num_samples`
5. Click `Generate Molecule`
6. Review the returned molecule cards and 3D viewers
7. Download `.sdf` files if needed

## Folder Outputs

Each generation request creates a folder like:

```text
jobs/3212f9e8/
```

Typical contents:

- uploaded `.pdb`
- one or more `.sdf` files
- `result.json`

That means the prototype keeps a simple file-based history of previous runs.

## Notes And Limitations

- This is a prototype, not a production service.
- Data storage is file-based, not database-backed.
- The frontend is implemented in a single HTML file for simplicity.
- CORS is fully open in the backend.
- Authentication and user management are not implemented.
- The live PMDM path depends on external Colab or Drive setup.
- The GNN evaluation section is currently static UI content.

## Which File Should Someone Read First?

- Read `README.md` for the project overview
- Read `SETUP_GUIDE.txt` for beginner setup steps
- Read `app.py` to understand backend behavior
- Read `web/index.html` to understand frontend behavior

## Plain-English Summary

This folder is a compact demo application that wraps a molecule-generation workflow in a browser interface.

The frontend collects a protein file from the user, the backend prepares or generates candidate molecules, RDKit computes useful chemistry metrics, and the UI shows the final molecules in 3D.
