export interface Shot {
    isMake: boolean;
    locationX: number;  // in feet
    locationY: number;  // in feet
  }
  
export interface Game {
    date: string;
    isStarter: boolean;
    minutes: number;
    points: number;
    assists: number;
    offensiveRebounds: number;
    defensiveRebounds: number;
    steals: number;
    blocks: number;
    turnovers: number;
    defensiveFouls: number;
    offensiveFouls: number;
    freeThrowsMade: number;
    freeThrowsAttempted: number;
    twoPointersMade: number;
    twoPointersAttempted: number;
    threePointersMade: number;
    threePointersAttempted: number;
    shots: Shot[];  // Array of shots
  }
  
export interface PlayerSummary {
    name: string;
    games: Game[];
  }