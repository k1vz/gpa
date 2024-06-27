# API Routes 

### Users
Request | Method | Route URI | Query | Cookies | Body | Response 
--- | --- | --- | --- | --- | --- |--- 
Register User |<div align="center">  ![GET](https://img.shields.io/badge/POST-yellow?style=flat) </div>| /users/register/ | <div align="center"> --- </div> | <div align="center">null</div> | ` { "email": string, "password": string } ` | ` {"id": int, "email": string} `
Login User |<div align="center">  ![GET](https://img.shields.io/badge/POST-yellow?style=flat) </div>| /users/login/ | <div align="center"> --- </div> | <div align="center">null</div> | ` { "email": string, "password": string } ` | ` { "jwt": string } `
Logout | <div align="center"> ![GET](https://img.shields.io/badge/GET-green?style=flat) </div>| /users/logout/ | <div align="center"> --- </div> | ` jwt=string ` | <div align="center">null</div> | ` {"message": string} `
Detail User | <div align="center"> ![GET](https://img.shields.io/badge/GET-green?style=flat) </div>| /users/detail/ |  <div align="center">` int `</div> | ` jwt=string ` | <div align="center">null</div> | ` {"id": int, "email": string} `
List All users | <div align="center"> ![GET](https://img.shields.io/badge/GET-green?style=flat) </div>| /users/ | <div align="center"> --- </div> | ` jwt=string ` | <div align="center">null</div> | ` [{"id": int, "email": string}] `