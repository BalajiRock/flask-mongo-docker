# Flask Basics
- Developed a basic flask application with mongoDB
- Implemented CRUD operations
## Key features
- Implemented caching to enhance the performance of CRUD operations
- Tried to achieve secure, optimal and scalable solution.

## API Endpoinds

- Create new user 
(HTTP Method POST)
    ```bash
    url - http://127.0.0.1:5000/users/
    Expected data format - {
            "id":2,
            "name":"Balaji Rock",
            "email":"balajiagmohan@gmail.com",
            "password":"12345678"
        }
    ```

- Update user 
(HTTP Method PUT)
    ```bash
    url - http://127.0.0.1:5000/users/<id>
    Expected data format - {
            "id":2,
            "name":"Balaji Rock",
            "email":"balajiagmohan@gmail.com",
            "password":"12345678"
        }
    ```

- Get user Details
(HTTP Method GET)
    ```bash
    url - http://127.0.0.1:5000/users/<id>
    ```

- Get All user names
(HTTP Method GET)
    ```bash
    url - http://127.0.0.1:5000/users/
    ```

- Remove user from database
(HTTP Method DELETE)
    ```bash
    url - http://127.0.0.1:5000/users/<id>
    ```


**Build and Run the Application:**
    ```bash
    docker-compose up --build
    ```
