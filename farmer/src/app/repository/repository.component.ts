import { Component, OnInit } from '@angular/core';
import { AuthService } from '../auth/auth.service';
import { Router } from '../../../node_modules/@angular/router';

@Component({
  selector: 'app-repository',
  templateUrl: './repository.component.html',
  styleUrls: ['./repository.component.css']
})
export class RepositoryComponent implements OnInit {


  constructor(private as: AuthService,
              private router: Router) { }

  ngOnInit() {
  }
  onBook(){
    //retrieve data from firebase
  }

}
