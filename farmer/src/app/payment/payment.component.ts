import { Component, OnInit } from '@angular/core';
import { AuthService } from '../auth/auth.service';
import { Router } from '../../../node_modules/@angular/router';

@Component({
  selector: 'app-payment',
  templateUrl: './payment.component.html',
  styleUrls: ['./payment.component.css']
})
export class PaymentComponent implements OnInit {

  constructor(private as: AuthService,
    private router: Router) { }

  ngOnInit() {
  }

  onPayment(){
    this.router.navigate(['page']);
  }

}
