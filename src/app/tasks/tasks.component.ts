import { Component } from '@angular/core';
import { ApiService } from 'src/services/api.service';

@Component({
  selector: 'app-tasks',
  templateUrl: './tasks.component.html',
  styleUrls: ['./tasks.component.css']
})
export class TasksComponent {
  title = "Tasks"
  
  data: any;

  loading = false;
  errorMsg = '';

  constructor(private api: ApiService) {}

  onButtonClick(): void {
    this.api.fetchData().subscribe({
      next: res => {
        console.log('res:', res)
        this.data = res;
        this.loading = false;
      },
      error: err => {
        this.errorMsg = `Oops! Couldn't fetch data in ${this.title}.`;
        console.error(err);
        this.loading = false;
      }
    })
  }
}
