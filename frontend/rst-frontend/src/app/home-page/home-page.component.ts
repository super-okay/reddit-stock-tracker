import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.scss']
})
export class HomePageComponent implements OnInit {

  constructor(private apiService:ApiService) { }

  ngOnInit(): void {
  }

  // gets stock price
  getStockPrice() {
    this.apiService.getStockPrice("GME").subscribe(
      (data:any) => {
        window.alert(data);
      },
      (error:any) => {
        console.log("Error getting stock price: " + error);
      }
    )
  }

}
