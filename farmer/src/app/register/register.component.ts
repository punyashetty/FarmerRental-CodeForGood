import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../auth/auth.service';


@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  fname:string;
  lname: string;
  username:string;
  password:string;
  confirm:string;
  phone:string;
  loc:string;


  constructor(private as: AuthService,
    private router: Router) { }

  ngOnInit() {
  }
  
  onRegister(fname:string,lname:string,username:string,password:string,confirm:string,phone:string,loc:string){
    this.as.register(this.fname,this.lname,this.username,this.password,this.confirm,this.phone,this.loc).then((user) =>{
      this.fname=fname;
      this.lname=lname;
      this.username=username;
      this.password=password;
      this.confirm=confirm;
      this.phone=phone;
      this.loc=loc;


    }).catch(error => console.log(error));
this.router.navigate(['login']);

  
}

}


