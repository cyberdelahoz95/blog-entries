# HTTP

## HTTP Requests

Angular provides it´s own module to process http request.
In order to use it, we must import the module from the app.module.ts file, then from the service or module we plan to use the http module we must import the service HttpClient.

It is important to remember that the http module of angular returns Observable objects, so in order to consume the result of the request we will need to use the method subscribe in order to have access to the data.

```javascript
  fetchProduct() {
    this.productsService.getAllProducts().subscribe((products) => {
      this.products = products;
    });
  }
```

We can easily map the response from a http request by declaring the desired type next to the method name.

```javascript
  getAllProducts() {
    return this.http.get<Product[]>(environment.url_api);
  }
```

the previous approach can be applied in many scenarios.

### Typing HTTP Responses

We can use an interface to assign a valid data type to the response coming from an API. This is a good practice to avoid certain type problems.

As an example to show how to type HTTP response, let's give our attention to the following interface.

```typescript
interface User {
  gender: string;
  email: string;
  phone: string;
}
```

User interface can be use as follows

```typescript
myFunction(): Observable<User[]>{
    return this.http.get("URL").pipe(
        map(
            (response:any) => response.results as User[]
            ))
}
```

### Handling errors

```typescript
this.http.get().pipe(
  retry(3), // try again 3 times
  catchError((error) => {
    return throwError("mensaje de error");
  })
  //normal flow
);
```

We use retry operator to avoid firing error immediately, instead we try 3 times and in case no success we process to call catchError operator to handle the exception.

### Downloading files

```typescript
getFile(){
    return this.http.get('URL.txt', {responseType:'text'})
        .subscribe(content => {})
}
```

Inside subscribe method we can handle a way of open a window or any other functionality to give the use the functionality to save the file.

### Interceptors

Interceptors are custom services used to add attributes to our HTTP request, like injecting tokens or add headers.

#### Steps to create an auth interceptor

1. Create a service using the command. _**ng g s auth**_
2. Rename the service to _**auth.interceptor.ts**_ and refactor any instruction related with the name we just changed.
3. Remove the line _**provideIn:'root'**_ this line is going to be found inside the _**auth.interceptor.ts**_ this line should be removed because we want to avoid this new service to be available all over the app but we want to limit it's use to certain scenarios.
4. Our new interceptor class should implements _**HttpInterceptor**_
5. Our logic is going to be implemented in the method _**intercept**_
6. In _**app.module.ts**_ we set manually our new interceptor class as a provider.

```typescript
// auth.interceptor.ts
export class AuthInterceptor implements HttpInterceptor {
  intercept(
    request: HttpRequest<any>,
    next: HttpHandler
  ): Observable<HttpEvent<any>> {
    request = request.clone({
      setHeaders: {
        myToke: "1234",
      },
    });
    return next.handle();
  }
}
```

```typescript
// app.module.ts
import { HTTP_INTERCEPTORS } from "@angular/common/http";
//import AuthInterceptor

providers: [
  {
    provide: HTTP_INTERCEPTORS,
    useClass: AuthInterceptor,
    multi: true,
  },
];
```

Note: If we want to use interceptor to store token, it is better to use _**indexDb**_ to store it rather than _**localStorage**_

If we want to store a token or some value in localStorage or any other local technology to store data we can proceed as follows.

```typescript
loginRestAPI(email:string, password: string){
    return this.http.post('URL',{email, password}).pipe(tap(dat) => {
        //store in local storage or any other strategy
    });
}
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE5NDIyMzIwMjddfQ==
-->
