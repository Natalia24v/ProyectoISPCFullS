import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './shared/header/header.component';
import { NavbarComponent } from './shared/navbar/navbar.component';
import { FooterComponent } from './shared/footer/footer.component';
import { TextoComponent } from './shared/texto/texto.component';
import { Texto2Component } from './shared/texto2/texto2.component';

@NgModule({
  declarations: [ 
    AppComponent,
    HeaderComponent,
    NavbarComponent,
    FooterComponent,
    TextoComponent,
    Texto2Component
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    

  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
