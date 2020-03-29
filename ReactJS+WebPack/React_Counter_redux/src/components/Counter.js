import React from 'react';
class Counter extends React.Component {
    render() {
        return (
            <div>
                <p style={{color: 'red'}}>
                    Click Time:{this.props.value}
                </p>
                <button onClick={this.props.add}>Add One</button>
                <button onClick={this.props.del}>Minus One</button>
            </div>
        )

    }
}

export default Counter;