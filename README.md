# Ice Cream Parlor Application

## Description
This is a simple Python application for a fictional ice cream parlor cafe that uses SQLite to manage:
- Seasonal flavor offerings
- Ingredient inventory
- Customer flavor suggestions and allergy concerns

## Features
As a user of the application, you should be able to:
- Maintain a cart of your favorite products
- Search & filter the offerings
- Add allergens if they don’t already exist

## Setup and Run the Application

### Prerequisites
- Python 3.9 or later
- Docker (if you want to run the application in a Docker container)

### Steps to Run the Application Locally

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd ice_cream_parlor
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Initialize the database:
    ```sh
    python database_setup.py
    ```

5. Run the application:
    ```sh
    python app.py
    ```

6. Open your web browser and navigate to `http://127.0.0.1:5000/`

### Steps to Run the Application using Docker

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd ice_cream_parlor
    ```

2. Build the Docker image:
    ```sh
    docker build -t ice_cream_parlor .
    ```

3. Run the Docker container:
    ```sh
    docker run -it --rm -p 5000:5000 --name ice_cream_parlor_app ice_cream_parlor
    ```

4. Open your web browser and navigate to `http://127.0.0.1:5000/`

## Test Steps
1. Run the application using the instructions above.
2. Use the navigation links to:
   - Search for seasonal flavors by entering a keyword in the search bar.
   - Add flavors to your cart from the search results.
   - View the items in your cart on the cart page.
   - Add a new allergen on the Add Allergen page.

## SQL Queries / ORM Abstraction
This application uses raw SQL queries to interact with the SQLite database. The `ice_cream_parlor.py` file contains the database interaction logic.

## Code Documentation
The code is documented with comments and is structured in a modular fashion for clarity and maintainability.

## Docker Commands
- To build the Docker image:
    ```sh
    docker build -t ice_cream_parlor .
    ```
- To run the Docker container:
    ```sh
    docker run -it --rm -p 5000:5000 --name ice_cream_parlor_app ice_cream_parlor
    ```

