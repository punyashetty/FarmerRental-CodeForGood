import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../auth/auth.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  username:string;
  password: string;
  

  constructor(private as: AuthService,
              private router: Router) { }

  ngOnInit() {
    
  }

  onLogin(username:string,password:string){
      this.as.login(this.username,this.password).then((user) =>{

        this.username=username;
        this.password=password;
        this.router.navigate(['book']);

      }).catch(error => console.log(error));

    
  }

  

}
