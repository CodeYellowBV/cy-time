import EntryOverview from 'screen/EntryOverview';
import NotFound from 'component/NotFound';
import { Entry } from 'store/Entry';
import { ProjectStore } from 'store/Project';
import moment from 'moment';

const PROJECT_DATA = [
    {
        id: 1,
        title: 'REX',
    },
    {
        id: 2,
        title: 'DOCC',
    },
];

export function home(store) {
    const projectStore = new ProjectStore().parse(PROJECT_DATA);
    store.setView({
        name: 'home',
        render: EntryOverview,
        currentEntry: new Entry({ startedAt: moment().format() }, { relations: ['project'] }),
        projectStore,
    });
}

export function notFound(store) {
    store.setView({
        name: 'notFound',
        render: NotFound,
    });
}
