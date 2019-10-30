import React from 'react';
class Counter extends React.Component {
    render() {
        return (
            <div>
                <p style={{color: 'red'}}>
                    Click Time:{this.props.value}
                </p>
                <button onClick={this.props.add}>加一</button>
                <button onClick={this.props.del}>减一</button>
            </div>
        )

    }
}

export default Counter;