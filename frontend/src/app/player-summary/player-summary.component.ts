import {
  ChangeDetectorRef,
  Component,
  OnDestroy,
  OnInit,
  ViewEncapsulation
} from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {untilDestroyed, UntilDestroy} from '@ngneat/until-destroy';
import {PlayersService} from '../_services/players.service';
import {PlayerSummary} from './player-summary.interface';
import { HttpClient } from '@angular/common/http';
import {ElementRef, Renderer2} from '@angular/core';
import { AfterViewInit } from '@angular/core';


@UntilDestroy()
@Component({
  selector: 'player-summary-component',
  templateUrl: './player-summary.component.html',
  styleUrls: ['./player-summary.component.scss'],
  encapsulation: ViewEncapsulation.None,
})
export class PlayerSummaryComponent implements OnInit, OnDestroy {

  public playerSummary: PlayerSummary;

  constructor(
    protected activatedRoute: ActivatedRoute,
    protected cdr: ChangeDetectorRef,
    protected playersService: PlayersService,
    private http: HttpClient,
    private elref: ElementRef,
    private renderer: Renderer2
  ) {

  }

  ngOnInit(): void {
    const playerID = this.activatedRoute.snapshot.paramMap.get('playerID');
    this.playersService.getPlayerSummary(1).pipe(untilDestroyed(this)).subscribe(data => {
      // console.log("Player Summary Log: ", data.apiResponse);
      this.playerSummary = data.apiResponse;

      this.http.get('assets/basketball-court.svg', { responseType: 'text' }).subscribe(svgData => {
        this.loadSvg(svgData);
      });

      this.cdr.detectChanges();
    });
  }
  

  ngOnDestroy() {
  }

  private loadSvg(svgData: string) {
    const svgContainer = this.elref.nativeElement.querySelector('#svg-container');
    this.renderer.setProperty(svgContainer, 'innerHTML', svgData);
    
    // Add shots after loading SVG
    for (const gameWrapper of this.playerSummary.games) {
      // console.log("GameWrapper: ", gameWrapper);
      // console.log("Game shots: ", gameWrapper[0].player_stats) 
            for (const shot of gameWrapper[0].player_stats.shots) {
              // console.log("shot: ", shot)
                const x = this.mapX(shot.locationY); // Mapping Y coord to X axis since the SVG is rotated 90 degrees in comparison to coordinate orientation.
                const y = this.mapY(shot.locationX); // Mapping X coord to Y axis ^^.
                this.addShot(x, y, shot.isMake);
            }
    }
}

private addShot(x: number, y: number, isMake: boolean) {
    const svg = this.elref.nativeElement.querySelector('svg > g > g');
    // console.log("SVG Element: ", svg);
    const circle = this.renderer.createElement('circle', 'svg');

    this.renderer.setAttribute(circle, 'cx', String(x));
    this.renderer.setAttribute(circle, 'cy', String(y));
    this.renderer.setAttribute(circle, 'r', '2');
    this.renderer.setAttribute(circle, 'fill', isMake ? 'green' : 'red');

    this.renderer.appendChild(svg, circle);
}

// Court is 94 feet long and 50 feet wide
// 94 feet : 512 pixels = ~5.447 pixels per foot
// 50 feet : 354 pixels (accounting for whitespace edges) = 7.08 pixels per foot. Each whitespace edge is 79 pixels.
// Backboard is 4 feet past the baseline = (4*5.447) = 21.788
// Basket's X coords = 21.788, Y coords = 79 + (354/2) = 256
private mapX(x: number): number {
    // Need to map x to proper coordinate on SVG
    return 21.788 + (x * 5.447);
}

private mapY(y: number): number {
    // Need to map y to proper coordinate on SVG
    return 256 + (y * 7.08);
}

}