import { AsyncPipe } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { Component, Injectable } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { Observable } from 'rxjs/internal/Observable';


interface Investment {
  titreoperation: string
  entreprise: string
  anneeDeLivraison: Number
  ville: string
  mandataire: string
  ppi: string
  lycee: string
  notificationDuMarche: string
  codeuai: string
  longitude: Number
  latitude: Number
  etatDAvancement: string
  montantDesApVotesEnMeu: Number
  caoAttribution: Date
  maitriseDOeuvre: string
  modeDeDevolution: string
  anneeDIndividualisation: Number
  enveloppePrevEnMeu: Number 
}

@Injectable({providedIn: 'root'})
@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet,AsyncPipe],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})



export class AppComponent {
  investments!: Investment[];

  constructor(private http: HttpClient) {   }


  getAllInvestments(): void {
    this.http.get<any>('/investment').subscribe(
      message => {
        this.investments = message.data;
      },
      err => {
        console.error('Imposible de récupérer les investissements:', err);
      }
    );
  }

  ngOnInit(): void {    
    this.getAllInvestments(); 
  }

}
