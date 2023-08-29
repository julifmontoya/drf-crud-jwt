
## 1. Project Goals
The purpose of this project is to create a Django Rest Framework API

## 2. Technologies I've used
- Python was used to write the functions and models as needed by the business logic.
- Django Rest Framework was used to create the project and app’s functionality (Models, Serializers and Views).

## 3. Database Design
This is the Relational Database used to create the models for the web application. 

## 4. User stories
###  4.1 Home
As a site user, I want to be able to publish or update posts.

###  4.2 Create Post
As a site user, I want to be able to create a post to publish on the blog. 

###  4.3 Update Post
As a site user, I want to be able to edit a post and make changes to its fields. 

###  4.4 Delete Post
As a site user, I want to be able to delete a post so that it no longer appears on the blog. 

## 5. API Reference

#### GET all post Public
```http
   https://http://127.0.0.1:8000/v1/posts/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
|  `None`   | `Array`  | Get all post               |

#### GET Detail post Public
```http
  https://http://127.0.0.1:8000/v1/posts/${id}/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |


#### GET all categories Public
```http
   https://http://127.0.0.1:8000/v1/categories/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
|  `None`   | `Array`  | Get all categories         |

#### POST Create Affiliate
```http
  https://http://127.0.0.1:8000/v1/affiliate/posts/create/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

{
    "title": "string",
    "description": "string",
    "user": "string",
    "category": "number"
}

#### GET Detail post Affiliate
```http
  https://http://127.0.0.1:8000/v1/affiliate/posts/${id}/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### PUT Detail post Affiliate
```http
  https://http://127.0.0.1:8000/v1/affiliate/posts/${id}/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

{
    "title": "string",
    "description": "string",
    "category": "number"
}

#### DELETE post Affiliate
```http
  https://http://127.0.0.1:8000/v1/affiliate/posts/${id}/delete/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

## 6. Testing
### 6.1 API Endpoints Testing
- I verify that all API endpoints are working correctly and returning the expected responses.
- Each endpoint was tested with different HTTP methods (GET, POST, PUT, DELETE) to ensure proper functionality.
- I check the appropriate status codes (e.g., 200 OK, 201 Created, 400 Bad Request, 404 Not Found) for different scenarios.

### 6.2 Input Validation Testing
- The input validation for all API endpoints corresponding with the fields of the models

### 6.3 Data Integrity Testing
- I verify the integrity of data stored in the database by performing CRUD (Create, Read, Update, Delete) operations through the API.
- I checked that data is saved correctly, updated accurately, and deleted successfully.
- I checked that data retrieval is returned for different scenarios.

### 6.4 Cross-Origin Resource Sharing (CORS) Testing:
- I verified that the appropriate CORS headers are included in API responses.