package com.example.punyashetty.kisaan;

import android.app.ProgressDialog;
import android.content.Intent;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.v7.app.AppCompatActivity;
import android.text.TextUtils;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.FirebaseNetworkException;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseAuthInvalidCredentialsException;
import com.google.firebase.auth.FirebaseAuthInvalidUserException;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

public class LoginActivity extends AppCompatActivity implements View.OnClickListener {


    //defining views
    String LOG_TAG="tag";
    private Button buttonSignIn;
    private EditText editTextEmail;
    private EditText editTextPassword;
    private TextView textViewSignup;
    String email;
    //firebase auth object
    private FirebaseAuth firebaseAuth;
    private DatabaseReference tRef;

    //progress dialog
    private ProgressDialog progressDialog;

    //database reference
    private DatabaseReference mData;

    private FirebaseAuth fire;


    static int flag=1;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
        tRef = FirebaseDatabase.getInstance().getReference();
        fire=FirebaseAuth.getInstance();
        //getting firebase auth object
        firebaseAuth = FirebaseAuth.getInstance();

        //if the objects getcurrentuser method is not null
        //means user is already logged in

        if(firebaseAuth.getCurrentUser() != null ){
            //close this activity
            finish();
            //opening profile activity
            //if(flag==0)
            tRef.addValueEventListener(new ValueEventListener() {
                @Override
                public void onDataChange(DataSnapshot dataSnapshot) {
                    //if logged in as consumer
                    DataSnapshot consumers = dataSnapshot.child("Consumer");
                    Iterable<DataSnapshot> AllConsumers = consumers.getChildren();
                    for (DataSnapshot var1 : AllConsumers) {
                        String emailFromFirebase = var1.getKey().toString();

                        String[] emailno = fire.getCurrentUser().getEmail().toString().split("\\.");
                        String e = emailno[0];
                        if (e.contains(emailFromFirebase)) {
                            //flag = 0;
                            //finish();


                        }

                    }

                    //if logged in as a farmer
                    DataSnapshot farmers = dataSnapshot.child("Farmer");
                    Iterable<DataSnapshot> AllFarmers = farmers.getChildren();
                    for (DataSnapshot var1 : AllFarmers) {
                        String emailforFarmer = var1.getKey().toString();
                        String[] emailno1 = fire.getCurrentUser().getEmail().toString().split("\\.");
                        String e1 = emailno1[0];
                        if (e1.contains(emailforFarmer)) {

                            //finish();


                        }

                    }

                }
                //       }     //}

                @Override
                public void onCancelled(DatabaseError databaseError) {

                }
            });
        }

        //initializing views
        editTextEmail = (EditText) findViewById(R.id.editText1);
        editTextPassword = (EditText) findViewById(R.id.editText2);
        buttonSignIn = (Button) findViewById(R.id.buttonSignin);
        textViewSignup  = (TextView) findViewById(R.id.textViewSignup);

        progressDialog = new ProgressDialog(this);

        //attaching click listener
        buttonSignIn.setOnClickListener(this);
        textViewSignup.setOnClickListener(this);
    }

    //method for user login
    private void userLogin(){
        email = editTextEmail.getText().toString().trim();
        String password  = editTextPassword.getText().toString().trim();


        //checking if email and passwords are empty
        if(TextUtils.isEmpty(email)){
            Toast.makeText(this,"Please enter email",Toast.LENGTH_LONG).show();
            return;
        }

        if(TextUtils.isEmpty(password)){
            Toast.makeText(this,"Please enter password",Toast.LENGTH_LONG).show();
            return;
        }

        //if the email and password are not empty
        //displaying a progress dialog

        progressDialog.setMessage("Logging in Please Wait...");
        progressDialog.show();

        //logging in the user

        firebaseAuth.signInWithEmailAndPassword(email,password)
                .addOnCompleteListener(LoginActivity.this, new OnCompleteListener<AuthResult>() {
                    @Override
                    public void onComplete(@NonNull Task<AuthResult> task) {

                        //if the task is successfull
                        if (task.isSuccessful()) {
                            progressDialog.dismiss();
                            //start the profile activity
                            Toast.makeText(getApplicationContext(), "Logged in successfully", Toast.LENGTH_SHORT).show();


                            tRef.addValueEventListener(new ValueEventListener() {
                                @Override
                                public void onDataChange(DataSnapshot dataSnapshot) {
                                    //if logged in as consumer
                                    DataSnapshot consumers = dataSnapshot.child("Consumer");
                                    Iterable<DataSnapshot> AllConsumers = consumers.getChildren();
                                    for (DataSnapshot var1 : AllConsumers) {
                                        String emailFromFirebase = var1.getKey().toString();
                                        String[] emailno = email.split("\\.");
                                        String e = emailno[0];
                                        if (e.contains(emailFromFirebase)) {
                                            //          flag = 0;
                                            finish();


                                            finish();
                                        }

                                    }
                                    // if (flag !=0 ) {
                                    //if logged in as a farmer
                                    DataSnapshot farmers = dataSnapshot.child("Farmer");
                                    Iterable<DataSnapshot> AllFarmers = farmers.getChildren();
                                    for (DataSnapshot var1 : AllFarmers) {
                                        String emailforFarmer = var1.getKey().toString();
                                        String[] emailno1 = email.split("\\.");
                                        String e1 = emailno1[0];
                                        if (e1.contains(emailforFarmer)) {

                                            finish();


                                            finish();
                                        }

                                    }

                                }
                                //}

                                @Override
                                public void onCancelled(DatabaseError databaseError) {

                                }
                            });
                        }



                        else
                        {
                            progressDialog.dismiss();
                            try {
                                throw task.getException();
                            } catch (FirebaseAuthInvalidUserException e) {
                                Log.d(LOG_TAG , "invalid id");
                            } catch (FirebaseAuthInvalidCredentialsException e) {
                                Log.d(LOG_TAG , e.getMessage().toString());

                            } catch (FirebaseNetworkException e) {

                            } catch (Exception e) {
                                Log.e(LOG_TAG, e.getMessage());
                            }

                            Toast.makeText(getApplicationContext(),"Invalid login!",Toast.LENGTH_SHORT ).show();

                        }
                    }
                });

    }

    @Override
    public void onClick(View view) {
        if(view == buttonSignIn){
            userLogin();
        }

        if(view == textViewSignup){
            //finish();
            //startActivity(new Intent(this, SignUpActivity.class));
        }
    }
    @Override
    public void onBackPressed(){
        Intent intent1 = new Intent(Intent.ACTION_MAIN);
        intent1.addCategory(Intent.CATEGORY_HOME);
        startActivity(intent1);
    }
}