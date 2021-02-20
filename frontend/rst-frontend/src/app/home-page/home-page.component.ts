import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.scss']
})
export class HomePageComponent implements OnInit {

  selectedTicker:string = "";

  constructor(private apiService:ApiService) { }

  ngOnInit(): void {
  }

  // gets stock price
  getStockPrice(selectedTicker:string) {
    this.apiService.getStockPrice(selectedTicker).subscribe(
      (data:any) => {
        window.alert(data.ticker);
      },
      (error:any) => {
        console.log("Error getting stock price: " + error);
      }
    )
  }

}
