import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../auth/auth.service';
import { DataService } from '../data.service';
import { Booking } from '../models/booking';
import { AngularFirestore } from '../../../node_modules/angularfire2/firestore';

@Component({
  selector: 'app-book',
  templateUrl: './book.component.html',
  styleUrls: ['./book.component.css']
})
export class BookComponent implements OnInit {
  machines: string;
  operator: string;
  sdate: Date;
  ddate: Date;
  Booking: any;

  bookComp : Booking = {} as Booking;
  constructor(private as: AuthService,private db: AngularFirestore,
    private router: Router, private ds: DataService) { 
      this.bookComp = null;
    }

  ngOnInit() {
    this.ds.getAllBookings().subscribe(docs => {
      console.log(docs);

    });
  }

  onBook(){
    this.router.navigate(['payment']);

    // const gh:Booking = {
    //   'id':this.Booking.id,
    //   'bookingId':this.Booking.bookingId,
    //   'endDate':this.Booking.endDate,
    //   'machine_id':this.Booking.machine_id,
    //   'operator':this.Booking.operator,
    //   'start_date':this.Booking.start_date
    // };


    

    // addBooking(booking: Booking){
    //   booking.id = this.db.createId();
    //   return this.db.collection('booking').doc(booking.id).set(booking);
    // }

    // this.ds.getAllBookings().subscribe(docs => {
    //      this.bookComp = this.db.collection('booking').valueChanges();   //which variable?
    // }

    // this.ds.
    
    //this.ds.getAllBookings().subscribe(docs => {                    //retreive data

    //})
  }
}
