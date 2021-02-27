import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.scss']
})
export class HomePageComponent implements OnInit {

  // stock data
  selectedTicker:string = "";
  submittedTicker:string = "";
  dataAtOpen:any;
  fullName:string = "";
  priceAtOpen:string = "";
  dateAtOpen:string = "";

  // reddit data
  numRedditPosts:number = -1;

  hasLoaded:boolean = false;

  constructor(private apiService:ApiService) { }

  ngOnInit(): void {
  }

  // gets stock price
  getStockData(selectedTicker:string) {
    this.apiService.getStockDataAPI(selectedTicker).subscribe(
      (data:any) => {
        // window.alert(JSON.stringify(data));
        this.submittedTicker = this.selectedTicker;
        this.dataAtOpen = data;
        this.fullName = data.fullName;
        this.priceAtOpen = data.open;
        this.dateAtOpen = data.date;
        this.hasLoaded = true;
      },
      (error:any) => {
        console.log("Error getting stock data: " + error);
      }
    )

    this.apiService.getRedditDataAPI(selectedTicker).subscribe(
      (data:any) => {
        this.numRedditPosts = data;
      },
      (error:any) => {
        console.log("Error getting reddit data: " + error)
      }
    )
  }

}
