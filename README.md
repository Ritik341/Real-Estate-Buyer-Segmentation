# Real Estate Buyer Segmentation – Unified Mentor Submission

## Project
**Machine Learning Based Buyer Segmentation and Investment Profiling for Real Estate Market Intelligence**

Internship organization: Unified Mentor  
Intern: Ritik Kumar Singh  
Role: Financial Analyst Intern

## Package contents
- `Project_2_Real_Estate_Buyer_Segmentation.ipynb` – original Jupyter/Colab notebook.
- `app.py` – Streamlit dashboard application.
- `data/Final_Real_Estate_Buyer_Segmentation.csv` – final buyer-level dataset used by the dashboard.
- `data/clients.csv` – original client data.
- `data/properties.csv` – original property transaction data.
- `requirements.txt` – Python dependencies.

## Run the dashboard locally
1. Install Python 3.10 or later.
2. Extract this ZIP file.
3. Open a terminal in the extracted project folder.
4. Install dependencies:

   `pip install -r requirements.txt`

5. Start the dashboard:

   `streamlit run app.py`

6. Open the local address printed by Streamlit (usually `http://localhost:8501`).

## Dataset checks
- Final buyer-level dataset: 2,000 rows × 23 columns.
- Client source dataset: 2,000 rows × 12 columns.
- Property source dataset: 10,000 rows × 9 columns.

## Important
The notebook is included as the supplied original notebook. The dashboard reads the final CSV from the `data` folder. Keep the `data` folder beside `app.py` after extracting the ZIP.

The public ngrok URL used during the demonstration is temporary and may expire when the Colab runtime or tunnel stops. For continuing access, deploy the app on a persistent hosting service and share that hosted URL.


## Final report and dashboard evidence
- `Unified_Mentor_Submission_Project_Report.pdf` – 58-page internship project report.
- `dashboard_screenshots/` – screenshots of the dashboard overview, KPIs, buyer segments, age distribution, geographic analysis, dataset preview and filter view.

## Demonstration dashboard
Current demo URL supplied for the internship submission:
https://shank-blame-armoire.ngrok-free.dev/

**Access note:** This is an ngrok tunnel URL and may stop working when its host/runtime is stopped. Confirm it is live immediately before sharing with Unified Mentor. For permanent access, deploy the Streamlit app to a persistent hosting service.
