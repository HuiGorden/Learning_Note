import React from 'react';
import ReactDOM from 'react-dom';
import Counter from './components/Counter';
import {createStore} from 'redux';
import reducer from './reducers/index';
import {numAdd,numDel} from './actions/index';

let store = createStore(reducer);
const initializer = () =>{
    ReactDOM.render(
        <Counter
            value={store.getState()}
            add ={()=>store.dispatch(numAdd())}
            del ={()=>store.dispatch(numDel())}
        />,
        document.getElementById('app')
    );
};

initializer();

store.subscribe(initializer);
