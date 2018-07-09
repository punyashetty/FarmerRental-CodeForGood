import { Injectable } from '@angular/core';
import { AngularFireAuth } from '../../../node_modules/angularfire2/auth';
import { AngularFireDatabaseModule, AngularFireDatabase} from 'angularfire2/database';
import { Router } from "@angular/router";
import * as firebase from 'firebase';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  authState: any = null;

  constructor(private afAuth: AngularFireAuth,
    private db: AngularFireDatabase,
    private router:Router) { 
      this.afAuth.authState.subscribe((auth) => {
        this.authState = auth
      });
    }

  login(username:string, password:string){
    return this.afAuth.auth.signInWithEmailAndPassword(username, password)
      .then((user) => {
        this.authState = user
        
      })
      
      .catch(error => console.log(error));
  }

  register(fname:string,lname:string,username:string,password:string,confirm:string,phone:string,loc:string){
    return this.afAuth.auth.createUserWithEmailAndPassword(username,password)
      .then((user) => {
        this.authState = user
        
      })
      .catch(error => console.log(error));
  }

  

  logout():void{
    this.afAuth.auth.signOut();
    this.router.navigate(['/'])
    }
      
  }
  


