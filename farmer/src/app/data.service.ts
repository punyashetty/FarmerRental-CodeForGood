import { Injectable } from '@angular/core';
import { AngularFirestore } from '../../node_modules/angularfire2/firestore';
import { Booking } from './models/booking';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  dataState:any =null;

  constructor(private db: AngularFirestore) {
   
    }
  
  // book(machines: string, operator: string, sdate: Date, ddate: Date){
  //   return this.db.auth.registerWithEmailAndPassword(username, password)
  //     .then((user) => {
  //       this.authState = user
        
  //     })
      
  //     .catch(error => console.log(error));
  // }

  addBooking(booking: Booking){
    booking.id = this.db.createId();
    return this.db.collection('booking').doc(booking.id).set(booking);
  }

  getAllBookings(){
    return this.db.collection<Booking>('booking').valueChanges();
  }

    payment(){
      
    }
  

}
