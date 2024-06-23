## API Routes 
  
Request | Method | Route URI | Cookies | Body | Response 
--- | --- | --- | --- | --- |--- 
SignUp User |<div align="center">  ![GET](https://img.shields.io/badge/POST-yellow?style=flat) </div>| /users/register/ | <div align="center">null</div> | ` { "email": string, "password": string } ` | ` {"id": int, "email": string} `
Login User |<div align="center">  ![GET](https://img.shields.io/badge/POST-yellow?style=flat) </div>| /users/login/ | <div align="center">null</div> | ` { "email": string, "password": string } ` | ` { "jwt": string } `
Get Token | <div align="center"> ![GET](https://img.shields.io/badge/GET-green?style=flat) </div>| /users/user/ | ` jwt=string ` | <div align="center">null</div> | ` {"id": int, "email": string} `
Logout | <div align="center"> ![GET](https://img.shields.io/badge/GET-green?style=flat) </div>| /users/logout/ | ` jwt=string ` | <div align="center">null</div> | ` {"message": string} `
  
<!-- Get Cards | <div align="center"> ![GET](https://img.shields.io/badge/GET-green?style=flat) </div>| /card | x-access-token=string | <div align="center">null</div> | ` [{ "cod": num, "front": string, "back": string, "interval_time": num, "review_cod": num }] ` -->