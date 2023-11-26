# Django Rest API Project 
Webová aplikace, co používá Django Rest API framework a Ubuntu Nginx server na DigitalOcean.

## Endpointy
### RestAPI
*api/author/*
 - Vrátí všechny autory v formátu JSON Id, Username, Password, Name, Surname
 - možnost napsat ***.json*** a subor lze stáhnout.
 
*api/author/username/<str:username>*
  - Vrátí jednoho autora podle username v formátu JSON, také lze napsat ***.json***
  
*api/blog/*
 - Vrátí všechny blogy v formátu JSON Id, Content, Date, Author{data autora}
 - možnost napsat ***.json*** a subor lze stáhnout.
 - Má možnost k GET a POST request.
 
*api/blog/blogId/<int:blog_id>*
 - Vrátí jeden blog podle id v formátu JSON, také lze napsat ***.json***
 - Má přistup k GET, PATCH a DELETE request.
 
*api/login/*
- Ednpoint na login, komunikuje s databázi. Vrácí 200 když všechno je ok, jinak vrací 404

*api/registration/*
- Endpoint na registraci, komunikuje s databázi, vrací 201 když všechno je ok, jinak vrací 400

### **BlogApp**
*login/*
- Ednpoint na login, dovoluje GET a POST requesty. GET renderuje html stránku, POST bere form inputy a posílá na *api/login/* pomocí POST requestu.

*registration/*
- Ednpoint na registraci, dovoluje GET a POST requesty. GET renderuje html stránku, POST bere form inputy a posílá na *api/registration/* pomocí POST requestu.

*homePage/*
- Renderuje html stránku s uživatelským účtem a formou na postování blogů.

*blogs/*
- Renderuje html stránku se všemi blogy

*logout/*
- Vymaže session a uživatel bude odhlašen. Redirectuje na *login/*

*postblog/*
- Přijme POST request z homePage a pošle POST request na *api/blog/*