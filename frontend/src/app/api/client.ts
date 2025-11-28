import { HttpClient } from '@angular/common/http';
import { inject, Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class Client {
  protected http = inject(HttpClient);

  getClientIp = (): Observable<any> => {
    return this.http.get<any>('http://localhost:8000/api/v1/todos/clientIp');
  };
}
