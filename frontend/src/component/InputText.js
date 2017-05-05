import PropTypes from 'prop-types';
import React, { Component } from 'react';
import { observer } from 'mobx-react';
import styled from 'styled-components';

const StyledInput = styled.input`
    width: 100%;
    height: 48px;
    border-radius: 8px;
    border: 0;
    padding: 0 8px;
`;

@observer
export default class InputText extends Component {
    static propTypes = {
        onChange: PropTypes.func.isRequired,
        name: PropTypes.string.isRequired,
        value: PropTypes.string,
    };

    static defaultProps = {
        value: '',
    };

    handleChange = e => {
        this.props.onChange(this.props.name, e.target.value);
    };

    render() {
        return (
            <StyledInput
                name={this.props.name}
                value={this.props.value}
                onChange={this.handleChange}
            />
        );
    }
}
