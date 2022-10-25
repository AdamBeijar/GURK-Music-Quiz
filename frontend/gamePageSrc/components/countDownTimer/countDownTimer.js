import React from 'react';
import {useState, useEffect} from 'react';
import {getRemainingTimeUntilMsTimestamp} from './Utils/CountdownTimerUtils';
import dayjs from 'dayjs';

const defaultRemainingTime = {
    seconds: '00',
    minutes: '00',
    hours: '00',
    days: '00'
}

const CountdownTimer = ({countdownTimestampMs, updateGameState}) => {
    const [remainingTime, setRemainingTime] = useState(defaultRemainingTime);
    
    useEffect(() => {
        const timestampDayjs = dayjs().add(countdownTimestampMs, 'milliseconds');
        const intervalId = setInterval(() => {
            updateRemainingTime(timestampDayjs);
        }, 1000);
        return () => clearInterval(intervalId);
    },[countdownTimestampMs]);

    function updateRemainingTime(countdown) {
        setRemainingTime(getRemainingTimeUntilMsTimestamp(countdown));
        if(remainingTime.seconds === "00") {
            console.log("Time's up!");
            updateGameState("game");
        }
    }

    return(
        <div className="countdown-timer">
            <span className="two-numbers">{remainingTime.seconds}</span>
            <span>seconds</span>
        </div>
    );
}

export default CountdownTimer;
