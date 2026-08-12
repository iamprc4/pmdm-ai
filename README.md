# Aushadh AI - PMDM Drug Discovery Platform

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**Aushadh AI** is an AI-powered drug discovery platform that generates novel drug molecules for protein targets using the PMDM (Protein-Molecule Dual Diffusion) model. Upload a protein structure, and the system generates optimized drug candidates with real-time 3D visualization and drug-likeness metrics.

---

## 🎯 Features

- **AI-Powered Molecule Generation**: Leverages PMDM dual diffusion model to generate drug candidates
- **3D Molecular Visualization**: Interactive 3D viewer for exploring generated molecules
- **Drug-Likeness Metrics**: Automatic calculation of QED, Lipinski rules, LogP, and molecular weight
- **Demo Mode**: Works with pre-generated molecules for quick demonstrations
- **Live Mode**: Integrates with Google Colab for real-time PMDM inference
- **REST API**: Full FastAPI backend for programmatic access
- **User-Friendly Interface**: Simple web UI for uploading proteins and viewing results

---

## 🏗️ Architecture

```
┌─────────────────┐
│   Frontend      │  Web interface (HTML/CSS/JS)
│   (index.html)  │
└────────┬────────┘
         │ HTTP/JSON
┌────────▼────────┐
│   FastAPI       │  Backend server (app.py)
│   Backend       │
└────────┬────────┘
         │
    ┌────┴────┐
    │         │
┌───▼──┐  ┌──▼────┐
│ Demo │  │ PMDM  │  AI Model (Colab)
│ Mode │  │ Live  │
└──────┘  └───────┘
```

---

## 📁 Project Structure

```
prototype/
├── app.py                      # Main FastAPI backend server
├── requirements.txt            # Python dependencies
├── SETUP_GUIDE.txt            # Detailed setup instructions
├── README.md                   # This file
│
├── web/                        # Frontend files
│   └── index.html             # Web interface
│
├── generated/                  # Generated molecules storage
│   └── source/                # Pre-generated demo .sdf files
│
├── uploads/                    # Uploaded .pdb files (auto-created)
├── jobs/                       # Job results storage (auto-created)
└── __pycache__/               # Python cache (auto-generated)
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- A modern web browser (Chrome, Firefox, Edge)

### Installation

1. **Clone or download this repository**
   ```bash
   cd prototype
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   If RDKit installation fails, try:
   ```bash
   pip install rdkit-pypi
   ```

3. **Add demo molecules** (optional, for demo mode)
   - Place `.sdf` files in `generated/source/`
   - You can download sample molecules from your Google Drive PMDM dataset

4. **Start the server**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to: `http://localhost:8000`

---

## 💻 Usage

### Demo Mode

The application works in **demo mode** by default if you have `.sdf` files in `generated/source/`. This is perfect for demonstrations without requiring the full PMDM model setup.

1. Download a sample protein structure:
   - [2VUK.pdb](https://files.rcsb.org/download/2VUK.pdb) (CDK2 - Cancer target)
   - [7L11.pdb](https://files.rcsb.org/download/7L11.pdb) (Mpro - COVID target)

2. Upload the `.pdb` file in the web interface

3. Set parameters:
   - **Atom budget**: Number of atoms (e.g., 20)
   - **Molecules to generate**: How many molecules (e.g., 3)

4. Click **Generate Molecules**

5. View results:
   - 3D interactive molecular structures
   - Drug-likeness metrics (QED, MW, LogP)
   - Lipinski rule compliance
   - Download individual `.sdf` files

### Live Mode (Advanced)

For real-time generation using the actual PMDM model:

1. Set up Google Colab with PMDM (see SETUP_GUIDE.txt)
2. Mount Google Drive
3. Configure paths in `app.py`:
   ```python
   DRIVE_BASE = pathlib.Path("/content/drive/MyDrive/PMDM")
   COLAB_PYTHON = "/content/micromamba/envs/pmdm/bin/python"
   COLAB_CKPT = DRIVE_BASE / "checkpoints" / "500.pt"
   ```

---

## 📊 API Endpoints

### Health Check
```http
GET /health
```
Returns server status and configuration.

### Generate Molecules
```http
POST /generate
Content-Type: multipart/form-data

Parameters:
- pdb_file: File (required) - Protein structure file
- num_atom: int - Number of atoms (default: 20)
- num_samples: int - Number of molecules to generate (default: 3)
```

### Get Job Results
```http
GET /job/{job_id}
```
Retrieve results for a specific generation job.

### Download SDF
```http
GET /sdf/{job_id}/{filename}
```
Download a specific molecule SDF file.

---

## 🧪 Understanding the Metrics

### QED (Quantitative Estimate of Drug-likeness)
- Range: 0.0 to 1.0
- **0.7+**: Excellent drug-likeness
- **0.5-0.7**: Good drug-likeness
- **< 0.5**: Poor drug-likeness

### Lipinski's Rule of Five
A molecule is likely to be orally bioavailable if:
- Molecular Weight (MW) ≤ 500 Da
- LogP ≤ 5
- H-bond donors (HBD) ≤ 5
- H-bond acceptors (HBA) ≤ 10

**Lipinski score** shows how many rules are satisfied (4/4 is ideal).

### Other Metrics
- **MW**: Molecular Weight in Daltons
- **LogP**: Lipophilicity (fat solubility)
- **SMILES**: Text representation of molecular structure

---

## 🔧 Configuration

### Change Server Port
```bash
python app.py --port 8001
```

### Environment Variables
You can configure the following in `app.py`:
- `DRIVE_BASE`: Google Drive path for PMDM model
- `COLAB_PYTHON`: Python interpreter path for Colab
- `COLAB_CKPT`: PMDM checkpoint file location
- `COLAB_REPO`: PMDM repository location

---

## 🐛 Troubleshooting

### "No molecules generated"
- **Cause**: No `.sdf` files in `generated/source/`
- **Fix**: Add sample `.sdf` files or configure live mode

### "Connection refused" at localhost:8000
- **Cause**: Server not running
- **Fix**: Run `python app.py` in terminal

### "ModuleNotFoundError: No module named 'rdkit'"
- **Cause**: RDKit not installed
- **Fix**: `pip install rdkit` or `pip install rdkit-pypi`

### Port 8000 already in use
- **Fix**: `python app.py --port 8001` then access `http://localhost:8001`

### RDKit installation fails
- **Try**: `pip install rdkit-pypi`
- **Or**: Use conda: `conda install -c conda-forge rdkit`

---

## 📦 Dependencies

- **FastAPI** (0.115+): Modern web framework for APIs
- **Uvicorn**: ASGI server for running FastAPI
- **python-multipart**: File upload support
- **RDKit** (2023.3.1+): Cheminformatics toolkit for molecular analysis

See `requirements.txt` for exact versions.

---

## 🎓 Use Cases

- **Drug Discovery**: Generate novel molecules for protein targets
- **Lead Optimization**: Explore chemical space around known drugs
- **Educational**: Learn about AI in drug discovery
- **Research**: Validate PMDM model performance
- **Presentations**: Demo AI-powered molecule generation

---

## 📈 Performance

### Demo Mode
- **Response Time**: < 2 seconds
- **Molecules**: Serves pre-generated structures
- **Use Case**: Demonstrations, testing UI

### Live Mode
- **Response Time**: 30-120 seconds (depends on GPU)
- **Molecules**: Real-time generation from PMDM
- **Use Case**: Production, research

---

## 🔒 Security Notes

- This is a prototype for educational/research purposes
- Not intended for production medical use
- Validate all generated molecules through proper drug discovery pipelines
- Do not use for actual patient treatment without proper approval

---

## 🤝 Contributing

This is a research prototype. For improvements:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

---

## 📝 License

This project is provided as-is for educational and research purposes. Please ensure compliance with:
- PMDM model license
- RDKit license (BSD)
- PDB database terms of use

---

## 🙏 Acknowledgments

- **PMDM Model**: Protein-Molecule Dual Diffusion framework
- **RDKit**: Open-source cheminformatics toolkit
- **PDB**: Protein Data Bank for structural data
- **FastAPI**: Modern Python web framework

---

## 📧 Support

For issues or questions:
1. Check `SETUP_GUIDE.txt` for detailed setup instructions
2. Review the troubleshooting section above
3. Check Python and dependency versions
4. Ensure all required files are in correct directories

---

## 🗺️ Roadmap

Potential future enhancements:
- [ ] Batch processing for multiple proteins
- [ ] Advanced filtering and sorting options
- [ ] Export results to various formats (CSV, JSON)
- [ ] Integration with molecular docking tools
- [ ] User authentication and job history
- [ ] Cloud deployment support
- [ ] Real-time progress indicators
- [ ] Molecular property prediction models

---

**Built with ❤️ for advancing AI-powered drug discovery**
