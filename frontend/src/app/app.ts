import { Component, inject, OnInit, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { Client } from './api/client';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet],
  templateUrl: './app.html',
  styleUrl: './app.scss'
})
export class App implements OnInit {
  protected readonly title = signal('angular-app');
  clientApi = inject(Client);
  public clientIp: string = '';

  ngOnInit(): void {
    this.getClientIp();
  }

  public getClientIp = () => {
    this.clientApi.getClientIp().subscribe(response => {
      this.clientIp = response.client_data;
    })
  }

}
