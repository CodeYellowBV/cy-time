import PropTypes from 'prop-types';
import React, { Component } from 'react';
import { observer } from 'mobx-react';
import UserOverviewItem from './UserOverviewItem';
import { EntryList } from '../component/EntryList';
import { UserStore } from '../store/User';

@observer
export default class UserOverview extends Component {
    static propTypes = {
        users: PropTypes.instanceOf(UserStore).isRequired,
    };

    renderUser(user) {
        return <UserOverviewItem key={user.id} user={user} />;
    }

    render() {
        return (
            <EntryList>
                {this.props.users.map(this.renderUser)}
            </EntryList>
        );
    }
}