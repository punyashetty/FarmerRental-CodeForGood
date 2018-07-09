import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../auth/auth.service';

@Component({
  selector: 'app-logout',
  templateUrl: './logout.component.html',
  styleUrls: ['./logout.component.css']
})
export class LogoutComponent implements OnInit {

  constructor( private router: Router, private as: AuthService) { }

  ngOnInit() {
   
  }

  onLogout(){
    this.as.logout();
    this.router.navigate(['/'])

  }

}

