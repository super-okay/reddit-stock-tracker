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
  fullName:string = "";

  dataAtOpen:any;
  priceAtOpen:string = "";
  dateAtOpen:string = "";

  dataAtClose:any;
  priceAtClose:string = "";
  dateAtClose:string = "";

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
        this.fullName = data.fullName;

        // data at open
        this.dataAtOpen = data.open;
        this.priceAtOpen = data.open.open;
        this.dateAtOpen = data.open.date;

        // data at close
        this.dataAtClose = data.close;
        this.priceAtClose = data.close.open;
        
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
