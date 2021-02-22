import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.scss']
})
export class HomePageComponent implements OnInit {

  selectedTicker:string = "";
  dataAtOpen:any;
  priceAtOpen:string = "";
  dateAtOpen:string = "";

  constructor(private apiService:ApiService) { }

  ngOnInit(): void {
  }

  // gets stock price
  getStockData(selectedTicker:string) {
    this.apiService.getStockDataAPI(selectedTicker).subscribe(
      (data:any) => {
        // window.alert(JSON.stringify(data));
        this.dataAtOpen = data;
        this.priceAtOpen = data.average;
        this.dateAtOpen = data.date;
      },
      (error:any) => {
        console.log("Error getting stock price: " + error);
      }
    )
  }

}
