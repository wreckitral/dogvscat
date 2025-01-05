# Dog vs. Cat Classifier  

A Flask-based application for binary classification to determine whether an uploaded image is of a dog or a cat.  

## Features  
- **Binary Classification**: Classifies images as either a dog or a cat.  
- **Dockerized**: Easily deployable using Docker for local development or production.  

## Prerequisites  
- Install [Docker](https://www.docker.com/get-started) on your system.  

## Getting Started  

### 1. Clone the Repository  
```bash  
git clone https://github.com/wreckitral/dogvscat.git
cd dogvscat
```  

### 2. Build the Docker Image  
Run the following command to build the Docker image:  
```bash  
docker build -t dog-cat-uas-ml .  
```  

### 3. Run the Application  
Start the application locally with:  
```bash  
docker run -p 5000:5000 dog-cat-uas-ml 
```  

### 4. Access the Application  
Once the application is running, you can access it in your browser at:  
```
http://localhost:5000  
```  

## Usage  
1. Open the application in your browser.  
2. Upload an image of a dog or a cat.  
3. The application will classify the image and display the result.  

## Troubleshooting  
If the application doesn't start:  
- Ensure Docker is installed and running.  
- Check for errors during the build or run process.  

## Contributing  
Feel free to submit issues or pull requests for improvements.  

## License  
This project is licensed under the [MIT License](LICENSE).  
