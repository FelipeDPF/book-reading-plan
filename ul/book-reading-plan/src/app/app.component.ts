import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';

import { CommonModule } from '@angular/common';
import { HttpClientModule, HttpClient } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, CommonModule, HttpClientModule, FormsModule, ReactiveFormsModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'Book Reading Plan';
  readingPlans: any[] = [];
  newBookPlan: { bookName: string; totalPages: number; targetDate: string } = {
    bookName: '',
    totalPages: 0,
    targetDate: ''
  };

  APIURL = 'http://localhost:8000/';

  constructor(private http: HttpClient) {}

  ngOnInit() {
    this.getReadingPlans();
  }

  getReadingPlans() {
    this.http.get(this.APIURL + 'get_reading_plans').subscribe((res: any) => {
      this.readingPlans = res;
    });
  }

  addReadingPlan() {
    const formData = new FormData();
    formData.append('book_name', this.newBookPlan.bookName);
    formData.append('total_pages', this.newBookPlan.totalPages.toString());
    formData.append('target_date', this.newBookPlan.targetDate);

    this.http.post(this.APIURL + 'add_reading_plan', formData).subscribe(() => {
      alert('Reading plan added successfully!');
      this.newBookPlan = { bookName: '', totalPages: 0, targetDate: '' };
      this.getReadingPlans();
    });
  }

  deleteReadingPlan(id: any) {
    const formData = new FormData();
    formData.append('id', id);

    this.http.post(this.APIURL + 'delete_reading_plan', formData).subscribe(() => {
      alert('Reading plan deleted successfully!');
      this.getReadingPlans();
    });
  }
}