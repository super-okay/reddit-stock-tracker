import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { retry, catchError, map} from 'rxjs/operators';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  url = "http://127.0.0.1:5000/"

  constructor(private http:HttpClient) { }

  // gets current price of stock
  getStockPrice(ticker:string) {
    return this.http.post(this.url+'/stocks', {ticker: ticker}).pipe(map(
      (data:any) => {
        return data;
      },
      (error:any) => {
        console.log(error);
      }
    ))
  }
}
