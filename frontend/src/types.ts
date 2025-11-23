export interface Driver {
    id: string;
    code?: string;
    team?: string;
    position: number;
    lapTime: string;
    winProbability: number;
    sectors?: {
        s1: number;
        s2: number;
        s3: number;
    };
    coordinates?: {
        x: number;
        y: number;
    };
    pitStops?: number;
    tyre?: string;
}

export interface Weather {
    condition: string;
    temp: number;
}

export interface RaceData {
    race: string;
    lap: number | string;
    totalLaps?: number;
    status?: string;
    weather?: Weather;
    drivers: Driver[];
}
