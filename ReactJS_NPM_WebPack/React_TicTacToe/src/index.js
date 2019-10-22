import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

class Square extends React.Component {
    render() {
        return (
            <button
                className="square"
                style={this.props.winningcell? {"backgroundColor": "yellow"}:{}}
                onClick={()=>this.props.onClick()}>
                {this.props.value}
            </button>
        );
    }
}

class Board extends React.Component {

    renderSquare(i) {
        return <Square
            winningcell={this.props.winnerLocation && this.props.winnerLocation.indexOf(i) !== -1? 1:0}
            value={this.props.squares[i]}
            onClick = {()=> this.props.onClick(i)}
        />;
    }

    render() {
        let layout = [];
        for(let i =0; i< this.props.squares.length; i = i+3){
            layout.push(<div className="board-row" key={i}>
                    {this.renderSquare(i)}
                    {this.renderSquare(i+1)}
                    {this.renderSquare(i+2)}
                </div>
                );
        }

        return (
            <div>
                {layout}
            </div>
        );
    }
}

class Game extends React.Component {

    constructor(props){
        super(props);
        this.state = {
            history: [{
                squares: Array(9).fill(null),
                row_number: null,
                col_number: null,
            }],
            stepNumber: 0,
            xIsNext: true,
            selectedBoldNumber: null,
            reverseHistory: false
        }
    }

    handleClick(i){
        const history = this.state.history.slice(0, this.state.stepNumber + 1);
        const current = history[history.length -1];
        const squares = current.squares.slice();
        const row_number = parseInt(i/3);
        const col_number = i%3;
        if(calculateWinner(squares)[0]||squares[i]){
            return;
        }
        squares[i] = this.state.xIsNext? "X": "O";
        this.setState({
            history: history.concat([
                {
                    squares: squares,
                    row_number: row_number,
                    col_number: col_number,
                }
            ]),
            stepNumber:history.length,
            xIsNext: !this.state.xIsNext,
            selectedBoldNumber: null
        });
    }

    jumpTo(step){
        this.setState({
            stepNumber: step,
            xIsNext: (step%2) === 0,
            selectedBoldNumber: step
        })
    }

    sortHistory(){
        this.setState({
            reverseHistory: !this.state.reverseHistory
        })
    }

    render() {
        const history = this.state.history;
        const current = history[this.state.stepNumber];
        let[winner, winner_location]= calculateWinner(current.squares) ;
        let moves = [];
        if (!this.state.reverseHistory) {
            moves = history.map((step, move) => {
                const desc = step.row_number != null && step.col_number != null ? "Go to move #" + move + `,(row:${step.row_number}, col:${step.col_number})` : "Go to game start";
                return <li key={move}>
                    <button onClick={() => this.jumpTo(move)}
                            style={this.state.selectedBoldNumber && this.state.selectedBoldNumber === move ? {"fontWeight": "bold"} : {}}>{desc}</button>
                </li>
            });
        }
        else{
            for(let i=history.length -1; i >=0; i--){
                let step = history[i];
                const desc = step.row_number != null && step.col_number != null ? "Go to move #" + i + `,(row:${step.row_number}, col:${step.col_number})` : "Go to game start";
                moves.push(<li key={i}>
                    <button onClick={() => this.jumpTo(i)}
                            style={this.state.selectedBoldNumber && this.state.selectedBoldNumber === i ? {"fontWeight": "bold"} : {}}>{desc}</button>
                </li>);
            }
        }
        let status;
        if (winner && winner !== "Draw"){
            status = <div>
                <p style={{"display":"inline"}}>"Winner: " + {winner}</p>
                <button style={{"display":"inline"}} onClick={(e) => {this.sortHistory()}}>Reverse Order</button>
            </div>
        }
        else if(winner && winner === "Draw"){
            status = <div>
                <p style={{"display":"inline"}}>Draw...Please Start Again</p>
                <button style={{"display":"inline"}} onClick={(e) => {this.sortHistory()}}>Reverse Order</button>
            </div>
        }
        else{
            status = <div>
                    <p style={{"display":"inline"}}> {"Next Play: " + (this.state.xIsNext? "X": "O")}</p>
                    <button style={{"display":"inline"}} onClick={(e) => {this.sortHistory()}}>Reverse Order</button>
                </div>
        }
        return (
            <div className="game">
                <div className="game-board">
                    <Board squares={current.squares} winnerLocation={winner_location} onClick={(i) => {this.handleClick(i)}}/>
                </div>
                <div className="game-info">
                    <div>{status}</div>
                    <ul>{moves}</ul>
                </div>
            </div>
        );
    }
}


ReactDOM.render(
    <Game />,
    document.getElementById('root')
);

function calculateWinner(squares) {
    const lines = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ];
    for (let i = 0; i < lines.length; i++) {
        const [a, b, c] = lines[i];
        if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
            return [squares[a],[a,b,c]];
        }
    }
    //Draw Logic
    let draw = true;
    for (let i =0; i <squares.length;i++){
        if (squares[i] === null){
            draw = false
        }
    }
    if (draw){
        return ["Draw", null];
    }
    //
    return [null, null];
}