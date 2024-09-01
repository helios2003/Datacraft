# Datacraft
This is a data visualization tool done as a part of the internship assignment for [Interface Labs](https://www.linkedin.com/company/interface-ai-labs/). Merchants/traders can upload their payment data and the web app crunches the tables and data to provide meaningful numbers and visualizations. <br /> <br />
You can find the hiring task [here](https://theinterfacecompany.notion.site/Full-Stack-Developer-SDE-Intern-87b68e73cdcd465fb4fbbe9b87e09570).

## Getting Started
### Setting it up Without Docker-Compose
- Clone the repository using the command
```
git clone https://github.com/helios2003/Datacraft.git
```
- Go into ``Datacraft`` directory.

#### Frontend
- Go into the ``frontend`` folder.
- Run ``npm install` to install the dependencies.
- Run ``npm run dev``. By default the frontend runs on ``http://localhost:8000``.

#### Backend
- Go into the ``backend`` folder.
- Create a [virtual environment](https://docs.python.org/3/library/venv.html) and activate it.
- Install the dependencies using the command ``pip install -r requirements.txt``.

#### Database
- Pull the PostgreSQL image from [DockerHub](https://hub.docker.com/_/postgres).
- Spin it up and connect it wiht the backend.

## Tasks Completed
### Data Processing
- [x] Create the Merged Sheet.
- [x] Group the dataset.
- [x] Create the 6 main tables.
- [x] Create the Tolerance Level table.
### Frontend
- [x] Make a responsive UI.
- [x] Use Typescript.
- [x] Create summaries and view the processed tables.

### Backend
- [x] Create endpoints for processing the uplaoding the dataset to database.
- [x] Functions for all the ELT processes.

### Deployment
- [x] Containerize the frontend, backend and the database.
- [x] Create the ``docker-compose.yml`` file.
- [x] Implement pre commit hooks.

## Tech Stack
- FastAPI in the backend + Pandas for the data preprocessing.
- NextJS in the frontend.
- PostgreSQL as the database.
  
  
