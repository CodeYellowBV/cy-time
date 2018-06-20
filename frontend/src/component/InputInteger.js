import PropTypes from 'prop-types';
import React, { Component } from 'react';
import { observer } from 'mobx-react';
import styled from 'styled-components';

const StyledInput = styled.input`
    width: 100%;
    height: ${props => (props.small ? '35' : '48')}px;
    border-radius: 8px;
    border: 0;
    padding: 0 8px;
`;

function isNumeric(n) {
  return !isNaN(parseFloat(n)) && isFinite(n);
}

@observer
export default class InputInteger extends Component {
    static propTypes = {
        onChange: PropTypes.func.isRequired,
        onBlur: PropTypes.func,
        name: PropTypes.string.isRequired,
        value: PropTypes.string,
        autoFocus: PropTypes.bool,
        small: PropTypes.bool,
    };

    static defaultProps = {
        value: '',
    };

    handleChange = e => {
        if(e.target.value.length > 4){
            e.target.value = e.target.value.replace('n', '');
            e.target.value = e.target.value.replace('u', '');
            e.target.value = e.target.value.replace('l', '');
            e.target.value = e.target.value.replace('l', '');
        }
        if(e.target.value.length === 0){
            e.target.value = 'null';
        }
        else if(!isNumeric(e.target.value)){
            return;
        }
        this.props.onChange(this.props.name, e.target.value);
    };

    render() {
        return (
            <StyledInput
                small={this.props.small}
                name={this.props.name}
                onBlur={this.props.onBlur}
                value={this.props.value}
                onChange={this.handleChange}
                autoFocus={this.props.autoFocus}
            />
        );
    }
}
