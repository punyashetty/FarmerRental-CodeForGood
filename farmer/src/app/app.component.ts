import { Component } from '@angular/core';
import { AuthService } from './auth/auth.service';
import { Router } from '../../node_modules/@angular/router';
import { AngularFireAuth } from '../../node_modules/angularfire2/auth';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'app';
  private isLoggedIn: Boolean;
  private user_displayName: String;
  private user_email: String;
  constructor(public authFire: AngularFireAuth, private router: Router) {

  }

  ngOnInit() {
    const auth = this.authFire.auth.currentUser;
    if (auth == null) {
      console.log("Logged out");
      this.isLoggedIn = false;
      this.user_displayName = '';
      this.user_email = '';
      this.router.navigate(['login']);
    } else {
      this.isLoggedIn = true;
      this.user_displayName = this.authFire.auth.currentUser.displayName;
      this.user_email = this.authFire.auth.currentUser.email;
      console.log("Logged in");
      console.log(auth);
      this.router.navigate(['book']);

    }
  }
}
