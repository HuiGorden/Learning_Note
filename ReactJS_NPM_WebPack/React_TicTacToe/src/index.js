import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

class Square extends React.Component {
    render() {
        return (
            <button
                className="square"
                onClick={()=>this.props.onClick()}>
                {this.props.value}
            </button>
        );
    }
}

class Board extends React.Component {

    renderSquare(i) {
        return <Square
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
                row: null,
                col: null
            }],
            stepNumber: 0,
            xIsNext: true,
            selectedBoldNumber: null
        }
    }

    handleClick(i){
        const history = this.state.history.slice(0, this.state.stepNumber + 1);
        const current = history[history.length -1];
        const squares = current.squares.slice();
        const row_number = parseInt(i/3);
        const col_number = i%3;
        if(calculateWinner(squares)||squares[i]){
            return;
        }
        squares[i] = this.state.xIsNext? "X": "O";
        this.setState({
            history: history.concat([
                {
                    squares: squares,
                    row_number: row_number,
                    col_number: col_number
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

    render() {
        const history = this.state.history;
        const current = history[this.state.stepNumber];
        const winner = calculateWinner(current.squares);

        const moves = history.map((step, move) =>{
            const desc = move ? "Go to move #" + move + `,(row:${step.row_number}, col:${step.col_number})`: "Go to game start";
            return <li key={move}>
                <button onClick={()=>this.jumpTo(move)} style={this.state.selectedBoldNumber && this.state.selectedBoldNumber === move? {"fontWeight":"bold"}: {}}>{desc}</button>
            </li>
        });
        let status;
        if (winner){
            status = "Winner: " + winner;
        }
        else{
            status = "Next Play: " + (this.state.xIsNext? "X": "O");
        }
        return (
            <div className="game">
                <div className="game-board">
                    <Board squares={current.squares} onClick={(i) => {this.handleClick(i)}}/>
                </div>
                <div className="game-info">
                    <div>{status}</div>
                    <ol>{moves}</ol>
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
            return squares[a];
        }
    }
    return null;
}