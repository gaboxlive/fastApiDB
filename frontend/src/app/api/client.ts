import { HttpClient } from '@angular/common/http';
import { inject, Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class Client {
  protected http = inject(HttpClient);

  getClientIp = (): Observable<any> => {
    return this.http.get<any>('http://192.168.1.68:8000/api/v1/todos/clientIp');
  };
}
