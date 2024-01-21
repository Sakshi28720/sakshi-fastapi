# Internship Take Home Assignment - Software Engineer


## Project Description
This project is a based upon FastAPI web service to segment images using custom MobileSAM model. This service allows user to upload an image which is then processed to generate a segmented version of the original image. 
To run the application, the user needs to install the dependencies and activate the virtual environment. 
The project's dependencies are stored in the requirements.txt file, and they can be installed using the pip command.
So, you just need to create and enter your virtual environment:

## FOR LINUX AND MACos USERS
- Open a terminal and go to the directory of your project repository.
- Inside your project repository, create a virtual environment with the Python venv module:
``` python -m venv env ```
- Now activate your virtual environment:
```source env/bin/activate```
(the command is different on Windows)
- Install dependencies in your virtual environment (activated) with the command:
```python -m pip install -r requirements.txt```

### FOR WINDOWS USERS
- Open a terminal and go to the directory of your project repository.
- Inside your project repository, create a virtual environment with the Python venv module:
``` python3 -m venv [Virtual Environment Name]```
- Now activate your virtual environment:
``` .\[Virtual Environment Folder Name]\Scripts\activate```
- Install dependencies in your virtual environment (activated) with the command:
```pip install -r requirements.txt```

**Features of the project**
Image Upload: Users can upload images for segmentation
Segmentation: Utilizes the MobileSAM mobile for image segmentation
Docker Integration: The services is containerize with Docker for easy deployement.

## Setup Instructions
### Prequisites
- Python 3.6 or higher
- Docker (for containerization)


## How to Run the Code

1. **In the terminal, navigate to the project. Here, the project is stored in the folder documents**

    ```bash
    USER:~$ cd Documents/spacesenseapp/mobilesam-task-main/ # cd path/to/your/project

    ```

2. **Install the Requirements**

    ```bash
    python -m pip install -r requirements.txt # On Windows use `pip install -r requirements.txt`

    ```

## Docker Installation
1. **Add Docker's official GPG key**
    ```bash
    sudo apt-get update
    sudo apt-get install ca-certificates curl gnupg
    sudo install -m 0755 -d /etc/apt/keyrings
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    sudo chmod a+r /etc/apt/keyrings/docker.gpg
    ```

2. **Add the Docker repository to APT sources**
    ```bash
    echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \ 
    $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
    sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    sudo apt-get update
    ```

3. **Install Docker engine**
    ```bash
    sudo apt-get install docker-ce docker-ce-cli containerd.io
    ```

4. **Verify docker engine is installed correctly**
    ```bash
    sudo docker run hello-world
    ```
    This command downloads a test image and runs it in a container. When the container runs, it prints a confirmation message and exits.


## Runnning the API service
1. **Run the FASTAPI server (without Docker)**

    ```bash
    uvicorn app:app --reload --port=8080 --host=0.0.0.0
    ```
2. **Build and Run the code with docker**
    ```bash
    docker compose up--build
    or 
    docker compose build --no-cache # this will disable cache for a fresh image
    ```

3. **Access the service**
    ```bash
    docker compose up #The FastAPI server will start, and the service will be available at http://localhost:8080.

    ```

10. **Stopping the service**
    ```bash
    docker compose down
    ```

## API Endpoints
1. GET /: The home page which provides the upload interface.
2. POST /uploadfile/: Endpoint to upload an image for segmentation.
