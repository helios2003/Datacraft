# Datacraft
This is a data visualization tool done as a part of the internship assignment for [Interface Labs](https://www.linkedin.com/company/interface-ai-labs/). Merchants/traders can upload their payment data and the web app crunches the tables and data to provide meaningful numbers and visualizations. <br /> <br />
You can find the hiring task [here](https://theinterfacecompany.notion.site/Full-Stack-Developer-SDE-Intern-87b68e73cdcd465fb4fbbe9b87e09570).

## Getting Started
- Clone the repository using the command
```
git clone https://github.com/helios2003/Datacraft.git
```
- Go into ``Datacraft`` directory.
### Setting it up With Docker-Compose
- Create a file named ``.env`` at the root and fill it with:
```
host_name="postgres"
```
- Run the command ``docker compose up -d``, This will help in creating and running all the 4 containers.
- The services will be available at the given ports as mentioned in the ``docker-compose.yaml``.

### Setting it up Without Docker-Compose

#### Frontend
- Go into the ``frontend`` folder.
- Run ``npm install` to install the dependencies.
- Run ``npm run dev``. By default the frontend runs on ``http://localhost:8000``.

#### Backend
- Go into the ``backend`` folder.
- Create a [virtual environment](https://docs.python.org/3/library/venv.html) and activate it.
- Install the dependencies using the command ``pip install -r requirements.txt``.
- Create a file named ``.env`` at the root and fill it with:
```
host_name="localhost"
```
#### Database
- Pull the PostgreSQL image from [DockerHub](https://hub.docker.com/_/postgres).
- Spin it up and connect it with the backend.
<br /> <br />
**To View the Tables in pgAdmin4** <br /> 
Follow the given steps
- In the home page of pgadmin4, click on ``Add Servers`` icon.
- This will open a pop up which contains few inputs to be given.
- Give the following inputs.
```conf
"Name": "local db",
"Group": "Server",
"Port": 5432,
"Username": "root",
"Host": "postgres_ilabs",
"SSLMode": "prefer",
"password": "example"
"MaintenanceDB": "postgres"
```
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
  

  
