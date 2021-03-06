import { createSlice } from '@reduxjs/toolkit';
import io from 'socket.io-client';

import constants from '../constants';
import { setFunds } from './funds';
import { orderIsExecuted, deletePendingOrder } from './orders';
import { updateStockRate } from './stocks';

let socket = null;

let initialState = false;
const socketSlice = createSlice({
    name: 'socket',
    initialState,
    reducers: {
        connect(_state, _action) {
            return true;
        },
        disconnect(_state, _action) {
            return false;
        },
    }
});

const { connect, disconnect } = socketSlice.actions;

export const connectSocket = (userToken) => {
    return (dispatch) => {
        if (socket === null || !socket.connected) {
            socket = io(constants.WEBSOCKET_DOMAIN);
            console.log(socket);
            socket.on('connect', () => {
                console.log("Connected!!!")
                dispatch(connect());
                socket.emit(constants.eventNewClient, { userToken });
            });
            socket.on(constants.eventStockRateUpdate, (data) => {
                console.log(constants.eventStockRateUpdate, data);
                dispatch(updateStockRate({ stockIndex: Number(data.stockIndex), newRate: Number(data.rate), time: data.time }));
            });
            socket.on(constants.eventOrderPlaced, (data) => {
                console.log(constants.eventOrderPlaced, data);
                if (data.ok) {
                    window.M.toast({ html: "Pending Order Successfully Executed", classes: "toast-success" });
                    dispatch(orderIsExecuted({ orderId: data.orderId, quantity: Number(data.quantity) }));
                    dispatch(setFunds(data.funds));
                } else {
                    dispatch(deletePendingOrder(data.orderId));
                    window.M.toast({ html: data.message, classes: "toast-error" });
                }
            });
        }
    };
};

export const disconnectSocket = () => {
    return (dispatch) => {
        if (socket !== null && socket.connected) {
            socket.disconnect();
        }
        dispatch(disconnect());
    };
};

export default socketSlice.reducer;
