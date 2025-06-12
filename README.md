# Transit Access API

This is a small, flexible API that calculates a basic public transit accessibility score for any given address. It's designed to support civic tech projects that aim to improve transportation equity, mobility planning, or local services.


> This project is in active development. Expect incomplete features, stubbed logic, and live updates.

---
## What You Can Do with This API

- Estimate how accessible a location is via public transit using real-world data
- Submit a street address and get a numeric "transit score" in response
- Integrate the API into apps, maps, or planning dashboards
- Adapt the scoring logic or data sources for your own city or use case
- Run it locally for testing or deploy it remotely as a public API

---
## Technologies Used
This project is built with:

- **Python** and **FastAPI** for the web framework
- **PostgreSQL** with optional **PostGIS** for spatial queries
- **GTFS static feeds** (e.g., LA Metro) and **OpenStreetMap** for data
- **Pytest** for testing
- **Docker** for containerized deployment (optional)

---
## Getting Started

This section assumes basic familiarity with Python and the terminal.

### 1. Clone the repository

```bash
git clone https://github.com/ryanfkeller/transit-access-api.git
cd transit-access-api
```

### 2. Set up your environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Set your environment variables
Create a `.env` file using the provided example: 
```bash
cp .env.example .env
```
Add your database URL and any API keys if needed. 

### 4. Run the server
```bash
uvicorn app.main:app --reload
```
This will start the API locally at `http://127.0.0.1:8000`

---
## Planned Endpoints
| Method | Endpoint      | Description                       |
| ------ | ------------- | ----------------------------------- |
| GET    | `/health`     | Confirms the server is running      |
| POST   | `/score`      | Accepts an address, returns a score |
| GET    | `/score/{id}` | Returns a previous result by ID     |

---
## Running Tests
To run the test suite, execute the following at under `transit-access-api/`:
```bash
pytest
```
Tests will live under the `/tests` directory, and will cover core logic and routes.

---
## Data Sources

This API relies on open datasets, including:

- [OpenStreetMap](https://www.openstreetmap.org) — for geocoding and location data
  - © OpenStreetMap contributors. Data available under the [Open Database License (ODbL)](https://opendatacommons.org/licenses/odbl/1-0/).
- [Transitland](https://transit.land/) — registry of GTFS feeds  
- [LA Metro GTFS](https://developer.metro.net/gtfs/) — example feed for scoring  

You can use your own city’s GTFS feed by replacing the static files.

---
## Why This Exists

Public transit is a lifeline — but access isn’t equal everywhere.  
This tool offers a basic way to quantify how reachable a location is by bus or rail.  
It’s a small piece that could plug into larger tools for city planners, nonprofits, or anyone working on transit equity.

---
## License

This project is open source under the MIT License.  
See `LICENSE` for details.

---
## About the Author

Built by [Ryan Keller](https://github.com/ryanfkeller), an engineer transitioning from the aerospace industry into public interest tech, with a focus on civic infrastructure and equity tools.
